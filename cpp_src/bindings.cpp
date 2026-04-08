#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;

extern std::vector<float> compute_viewshed(const std::vector<float>&, int, int, int, int, float, int, int);
extern std::vector<int> classify_terrain(const std::vector<float>&, int, int, float, float);

PYBIND11_MODULE(perception_core, m) {
    m.def("compute_viewshed", &compute_viewshed, "Ray-cast line-of-sight viewshed");
    m.def("classify_terrain", &classify_terrain, "Slope-based terrain classification");
}