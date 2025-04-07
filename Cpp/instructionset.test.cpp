#include <iostream>
#include <immintrin.h> // For AVX intrinsics

void avxVectorAdd(float* a, float* b, float* result, int size) {
    for (int i = 0; i < size; i += 8) {
        __m256 va = _mm256_loadu_ps(&a[i]); // Load 8 floats from a
        __m256 vb = _mm256_loadu_ps(&b[i]); // Load 8 floats from b
        __m256 vresult = _mm256_add_ps(va, vb); // Add 8 floats in parallel
        _mm256_storeu_ps(&result[i], vresult); // Store the result
    }
}

int main() {
    int size = 16;
    float a[16] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f, 11.0f, 12.0f, 13.0f, 14.0f, 15.0f, 16.0f};
    float b[16] = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f};
    float result[size];

    avxVectorAdd(a, b, result, size);

    for(int i = 0; i < size; ++i){
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}