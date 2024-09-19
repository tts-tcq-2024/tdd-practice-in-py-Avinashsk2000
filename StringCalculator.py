static int add(const char* input) {
    // If input is NULL or an empty string, return 0
    if (input == NULL || *input == '\0') {
        return 0;
    }
    // Existing logic for non-empty input
    char delimiters[3];  
    char negatives[256] = {0};  
    const char* numbersPart = extractCustomDelimiter(input, delimiters);
    return sumNumbers(numbersPart, delimiters, negatives);
}
