
from collections import defaultdict

prevBounds = defaultdict(str)
prevBounds["2mm"] = r'\frac{2 N_i N_j (N_k + N_l)}{\sqrt{S}}'
prevBounds["3mm"] = r'\frac{2 N_i (N_j N_k + N_i N_l + N_l N_m)}{\sqrt{S}}'
prevBounds["adi"] = r'N^2 T'
prevBounds["atax"] = r'M N'
prevBounds["bicg"] = r'M N'
prevBounds["cholesky"] = r'\frac{N^3}{6 \sqrt{S}}'
prevBounds["correlation"] = r'\frac{M^2 N}{2 \sqrt{S}}'
prevBounds["covariance"] = r'\frac{M^2 N}{2 \sqrt{S}}'
prevBounds["deriche"] = r'H W'
prevBounds["doitgen"] = r'\frac{2 N_q N_r N_p^2}{\sqrt{S}}'
prevBounds["durbin"] = r'\frac{N^2}{2}'
prevBounds["fdtd"] = r'\frac{N_x N_y T}{2 \sqrt{2} \sqrt{S}}'
prevBounds["floyd-warshall"] = r'\frac{N^3}{\sqrt{S}}'
prevBounds["gemm"] = r'\frac{2 N_i N_j N_k}{\sqrt{S}}'
prevBounds["gemver"] = r'N^2'
prevBounds["gesummv"] = r'2 N^2'
prevBounds["gramschmidt"] = r'\frac{M N^2}{\sqrt{S}}'
prevBounds["heat"] = r'\frac{9 \sqrt[3]{3} N^3 T}{16 \sqrt[3]{S}}'
prevBounds["jacobi1d"] = r'\frac{N T}{4 S}'
prevBounds["jacobi2d"] = r'\frac{2 N^2 T}{3 \sqrt{3} \sqrt{S}}'
prevBounds["lu"] = r'\frac{2 N^3}{3 \sqrt{S}}'
prevBounds["ludcmp"] = r'\frac{2 N^3}{3 \sqrt{S}}'
prevBounds["mvt"] = r'N^2'
prevBounds["nussinov"] = r'\frac{N^3}{6 \sqrt{S}}'
prevBounds["seidel"] = r'\frac{2 N^2 T}{3 \sqrt{3} \sqrt{S}}'
prevBounds["symm"] = r'\frac{2 M^2 N}{\sqrt{S}}'
prevBounds["syr2k"] = r'\frac{M N^2}{\sqrt{S}}'
prevBounds["syrk"] = r'\frac{M N^2}{2 \sqrt{S}}'
prevBounds["trisolv"] = r'\frac{N^2}{2}'
prevBounds["trmm"] = r'\frac{M^2 N}{\sqrt{S}}'
prevBounds['conv'] = r'\frac{C_{\mathrm{out}}\,H_{\mathrm{out}}\,S\,W_{\mathrm{out}}\,\mu \,\left(2\,C_{\mathrm{in}}\,H_{\mathrm{ker}}\,W_{\mathrm{ker}}-1\right)}{2\,S\,\mu -\mu +8\,\sqrt{2}\,\sqrt{H_{\mathrm{ker}}}\,S^{3/2}\,\sqrt{W_{\mathrm{ker}}}}-\frac{1}{S}'

polybenchRes = {}
polybenchRes["2mm"] =                          ["2*NI*NJ*(NK + NL)/sqrt(S)"]
polybenchRes["3mm"] =                          ["2*NJ*(NI*NK + NI*NL + NL*NM)/sqrt(S)"]
polybenchRes["atax"] =                         ["M*N"]
polybenchRes["bicg"] =                         ["M*N"]
polybenchRes["cholesky"] =                     ["N^3/(3*sqrt(S))"]
polybenchRes["correlation"] =                  ["M^2*N/sqrt(S)"]
polybenchRes["covariance"] =                   ["M^2*N/sqrt(S)", "M^2*N/sqrt(S) + M*N"]
polybenchRes["deriche"] =                      ["3*H*W"]
polybenchRes["doitgen"] =                      ["2*NP^2*NQ*NR/sqrt(S)"]
polybenchRes["durbin"] =                       ["3*N^2/2"]
polybenchRes["fdtd2d"] =                       ["2*sqrt(3)*T*NX*NY/sqrt(S)", "2*sqrt(2)*T*NX*NY/sqrt(S)"]
polybenchRes["floyd-warshall"] =               ["2*N^3/sqrt(S)"]
polybenchRes["gemm"] =                         ["2*NI*NJ*NK/sqrt(S)"]
polybenchRes["gemver"] =                       ["N^2"]
polybenchRes["gesummv"] =                      ["2*N^2"]
polybenchRes["gramschmidt"] =                  ["M*N^2/sqrt(S)", "2*M*N^2/sqrt(S)"]
polybenchRes["heat3d"] =                       ["6*N^3*T/S^(1/3)"]
polybenchRes["jacobi1d"] =                     ["2*N*T/S"]
polybenchRes["jacobi2d"] =                     ["4*N^2*T/sqrt(S)"]
polybenchRes["lu"] =                           ["2*N^3/(3*sqrt(S))"]
polybenchRes["ludcmp"] =                       ["2*N^3/(3*sqrt(S))"]
polybenchRes["mvt"] =                          ["N^2"]
polybenchRes["nussinov"] =                     ["N^3/(3*sqrt(S))", "N^2*(sqrt(S) + S*(N - 3)/3)/S^(3/2)"]
polybenchRes["seidel2d"] =                     ["4*N^2*T/sqrt(S)"]
polybenchRes["symm"] =                         ["sqrt(2)*M^2*N/sqrt(S)", "2*M^2*N/sqrt(S)", "M^2*N/sqrt(S)"]
polybenchRes["syr2k"] =                        ["2*M*N^2/sqrt(S)"]
polybenchRes["syrk"] =                         ["M*N^2/sqrt(S)"]
polybenchRes["trisolv"] =                      ["N^2/2"]
polybenchRes["trmm"] =                         ["M^2*N/sqrt(S)"]