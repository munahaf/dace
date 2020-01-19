#ifndef __DACE_PERF_REPORTING_H
#define __DACE_PERF_REPORTING_H

#include <chrono>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>

namespace dace {
namespace perf {

    /**
     * Simple instrumentation report class that can save to JSON.
     */
    class Report {
    protected:
        std::map<std::string, std::vector<double> > _fields;
    public:
        Report() : _fields() {}
        ~Report() {}

        /**
         * Appends a single result to the report.
         * @param name: Name of the category.
         * @param value: Value to save.
         */
        void add(const char *name, double value) {
            this->_fields[name].push_back(value);
        }

        /**
         * Saves the report to a timestamped JSON file.
         * @param path: Path to folder where the output JSON file will be stored.
         */
        void save(const char *path) {
            // Create report filename
            std::stringstream ss;
            std::chrono::milliseconds ms = std::chrono::duration_cast<std::chrono::milliseconds>(
            std::chrono::system_clock::now().time_since_epoch());
            ss << path << "/" << "report-" << ms.count() << ".json";

            // Dump report as JSON
            {
                bool first = true;
                std::ofstream ofs (ss.str(), std::ios::binary);
                ofs << "{" << std::endl;
                for (const auto& kv : this->_fields) {
                    if (first)
                        first = false;
                    else
                        ofs << "," << std::endl;
                    ofs << "  \"" << kv.first << "\": [";
                    bool first_elem = true;
                    for (const auto& value : kv.second) {
                        if (first_elem)
                            first_elem = false;
                        else
                            ofs << ", ";
                        ofs << value;
                    }
                    ofs << "]";
                }
                ofs << std::endl << "}" << std::endl;
            }
        }
    };


}  // namespace perf
}  // namespace dace

#endif  // __DACE_PERF_REPORTING_H
