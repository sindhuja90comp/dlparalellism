#include <iostream>
#include <chrono>
#include <vector>

void scalarVectorAdd(const std::vector<float>& a, const std::vector<float>& b, std::vector<float>& result) {
    for (size_t i = 0; i < a.size(); ++i) {
        result[i] = a[i] + b[i];
    }
}

int main() {
    size_t size = 1024 * 1024; // Large dataset
    std::vector<float> a(size, 1.0f);
    std::vector<float> b(size, 2.0f);
    std::vector<float> result(size);

    auto start = std::chrono::high_resolution_clock::now();
    scalarVectorAdd(a, b, result);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;
    std::cout << "Scalar addition time: " << duration.count() << " seconds" << std::endl;

    return 0;
}