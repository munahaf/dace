import copy
import math
import ast
import numpy as np
import random
import string

from typing import Any, Generator, Tuple

from dace import SDFG, nodes, symbolic
from dace.sdfg.analysis import cutout as cutter
from dace.optimization.transfer_tuning.transfer_space import TransferSpace
from dace.transformation import helpers as xfh
from dace.transformation.dataflow import MapTiling

class MapTilingSpace(TransferSpace):

    def name(self) -> str:
        return 'MapTilingSpace'

    def apply_config(self, cutout: SDFG, config: Any, make_copy: bool = True) -> SDFG:
        if make_copy:
            cutout_ = copy.deepcopy(cutout)
        else:
            cutout_ = cutout
        
        param, target = config
        state_id, node_id = target
        map_entry = cutout.node(state_id).node(node_id)

        MapTiling.apply_to(
            cutout_,
            map_entry=map_entry,
            options={"tile_sizes": param},
            verify=False,
            save=False,
            annotate=False,
        )

        return cutout_

    def translate_config(self, cutout: SDFG, sdfg: SDFG, config: Any) -> Any:
        param, target = config
        state_id, node_id = target
        map_entry = cutout.node(state_id).node(node_id)

        sstate_id = cutout.name.split("_")[-1]
        snode_id = sdfg.node(sstate_id).node_id(map_entry)
        return param, (sstate_id, snode_id)

    def encode_config(self, config: Any) -> str:
        return str(config)

    def decode_config(self, config: str) -> Any:
        return ast.literal_eval(config)

    def extract_patterns(self, sdfg: SDFG, cutout: SDFG, config: str) -> Tuple[Tuple[Any, str]]:
        state_id = int(cutout.name.split("_")[-1])
        state = sdfg.node(state_id)
        
        map_entry = MapTilingSpace.top_map(cutout)
        node_id = state.node_id(map_entry)
        
        letters = string.ascii_lowercase
        embedding = ''.join(random.choice(letters) for i in range(10))
        pattern = {
            # "embedding": np.zeros((2,), dtype=np.float32),
            "embedding": embedding,
            "config": config,
            "sdfg": sdfg.hash_sdfg(),
            "target": [(state_id, node_id)]
        }
        return (
            pattern,
        )

    def cutouts(self, sdfg: SDFG) -> Generator[SDFG, None, None]:
        for state in sdfg.nodes():
            for node in state.nodes():
                if not isinstance(node, nodes.MapEntry) or xfh.get_parent_map(state, node) is not None:
                    continue
            
                state_id = sdfg.node_id(state)
                subgraph_nodes = state.scope_subgraph(node).nodes()
                cutout = cutter.cutout_state(state, *subgraph_nodes, make_copy=False)
                yield cutout

    def configurations(self, cutout: SDFG) -> Generator[Any, None, None]:
        map_entry = MapTilingSpace.top_map(cutout)
        
        state_id = 0
        node_id = cutout.start_state.node_id(map_entry)
        
        max_tile = []
        for rng in map_entry.range.ranges:
            start, stop, step = rng
            iter = (stop - start) / step
            iter = int(symbolic.evaluate(iter, symbols=cutout.constants))

            max_tile.append(iter)

        for k in range(1, 11):
            param = []
            all_bounded = True
            for dim in max_tile:
                max_k = int(math.log2(dim)) 
                if max_k < k:
                    tile_size = 2 ** max_k
                else:
                    tile_size = 2 ** k
                    all_bounded = False
                
                param.append(tile_size)

            if all_bounded:
                break 

            yield param, (state_id, node_id)

    @staticmethod
    def top_map(cutout: SDFG):
        map_entry = None
        for node in cutout.start_state.nodes():
            if not isinstance(node, nodes.MapEntry) or xfh.get_parent_map(cutout.start_state, node) is not None:
                continue

            map_entry = node
            break
    
        return map_entry