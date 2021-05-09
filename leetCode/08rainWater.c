
int trap(int* height, int heightSize){
    
    int result = 0;

    int currentMaximum = 0;
    int tmp = 0;
    
    int i = 0;
    int bar = 0;

    for (i=0; i<heightSize; i++) {
        bar = height[i];
            
        if (bar >= currentMaximum) {
            result +=  tmp;

            currentMaximum = bar ;
            tmp = 0;
        } else {
            tmp += currentMaximum - bar;
        }
    }
    
    currentMaximum = 0;
    tmp = 0;
    
    for (i=heightSize - 1; i>=0; i--) {
        bar = height[i];

        if (bar > currentMaximum) {
            result +=  tmp;

            currentMaximum = bar ;
            tmp = 0;
        } else {
            tmp += currentMaximum - bar;
        }
    }
    return result;
}
