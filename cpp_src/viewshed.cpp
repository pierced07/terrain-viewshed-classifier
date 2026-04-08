#include <vector>
#include <cmath>
#include <algorithm>

std::vector<float> compute_viewshed(
    const std::vector<float>& terrain,
    int rows, int cols,
    int obs_x, int obs_y,
    float obs_height,
    int max_range,
    int n_angles
) {
    std::vector<float> viewshed(rows * cols, 0.0f);
    float angle_step = 2.0f * M_PI / n_angles;

    for (int a = 0; a < n_angles; ++a) {
        float angle = a * angle_step;
        float cos_a = std::cos(angle);
        float sin_a = std::sin(angle);
        float max_elev = -1e9f;

        for (int step = 1; step < max_range; ++step) {
            int x = obs_x + static_cast<int>(cos_a * step);
            int y = obs_y + static_cast<int>(sin_a * step);

            if (x >= 0 && x < rows && y >= 0 && y < cols) {
                float dist = std::hypot(x - obs_x, y - obs_y);
                if (dist < 0.1f) continue;

                float elev = std::atan2(terrain[x * cols + y] - obs_height, dist);
                if (elev > max_elev) {
                    max_elev = elev;
                    viewshed[x * cols + y] = 1.0f;
                }
            }
        }
    }
    return viewshed;
}