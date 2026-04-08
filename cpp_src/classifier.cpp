#include <vector>
#include <cmath>

std::vector<int> classify_terrain(
    const std::vector<float>& terrain,
    int rows, int cols,
    float flat_thresh_deg,
    float steep_thresh_deg
) {
    std::vector<int> classification(rows * cols, 1);
    float rad_to_deg = 180.0f / M_PI;

    for (int x = 1; x < rows - 1; ++x) {
        for (int y = 1; y < cols - 1; ++y) {
            float gx = (terrain[x * cols + (y+1)] - terrain[x * cols + (y-1)]) * 0.5f;
            float gy = (terrain[(x+1) * cols + y] - terrain[(x-1) * cols + y]) * 0.5f;
            float slope_rad = std::atan2(std::hypot(gx, gy), 1.0f);
            float slope_deg = slope_rad * rad_to_deg;

            int idx = x * cols + y;
            if (slope_deg <= flat_thresh_deg) classification[idx] = 1;
            else if (slope_deg <= steep_thresh_deg) classification[idx] = 2;
            else classification[idx] = 3;
        }
    }
    return classification;
}