class Solution {
public:
    int findKthNumber(int n, int k) {
        int current = 1;  // Start with the first number in lexicographical order
        k--;              // Decrement k since we consider the first element

        // Continue until we find the k-th number
        while (k > 0) {
            long long steps = calculateSteps(n, current, current + 1);
            
            if (steps <= k) {
                // If the k-th number is not within this prefix, move to the next prefix
                current++;
                k -= steps;
            } else {
                // If within the current prefix, move down to the next level
                current *= 10;
                k--;
            }
        }

        return current;
    }

private:
    // Helper function to calculate the number of steps between two prefixes
    long long calculateSteps(int n, long long first, long long last) {
        long long steps = 0;

        while (first <= n) {
            steps += std::min(static_cast<long long>(n + 1), last) - first;
            first *= 10;
            last *= 10;
        }

        return steps;
    }
};
