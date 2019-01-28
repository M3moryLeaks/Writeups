trainedData = 'myLang/tessdata/alien.traineddata';
layout = 'Block';

f = fopen('result.txt', 'w');
I = imread('alienMessage.png');

results = ocr(I, 'Language', trainedData, 'TextLayout', layout);

fprintf(f, results.Text);
fclose(f);