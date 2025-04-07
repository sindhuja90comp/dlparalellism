#include <iostream>
#include <chrono>
#include <vector>

void unrolledAdd(const std::vector<float>& a, const std::vector<float>& b, std::vector<float>& result) {
    size_t size = a.size();
    for (size_t i = 0; i < size; i += 4) {
        result[i] = a[i] + b[i];
        result[i + 1] = a[i + 1] + b[i + 1];
        result[i + 2] = a[i + 2] + b[i + 2];
        result[i + 3] = a[i + 3] + b[i + 3];
    }
}

int main() {
    size_t size = 1024 * 1024;
    std::vector<float> a(size, 1.0f);
    std::vector<float> b(size, 2.0f);
    std::vector<float> result(size);

    auto startUnrolled = std::chrono::high_resolution_clock::now();
    unrolledAdd(a, b, result);
    auto endUnrolled = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> durationUnrolled = endUnrolled - startUnrolled;
    std::cout << "Unrolled time: " << durationUnrolled.count() << " seconds" << std::endl;

    return 0;
}