// #3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".


for(var i = 1;i<=100; i++) {
    if (i%10==0){
    console.log("Coding Dojo")}
    else if (i%5==0){
    console.log("Coding")}
    else {
    console.log(i)}
}

Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for(var i = 2018;i>0; i=i-4) {
    console.log(i);
}
for j in Range(2018,0,-4)
    print(j)

    # Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

i=2
while(i < 9);
    i++;
    if(i/3==0){
        console.log(i);
    }

function lowHighMult(lowNum, highNum, mult){
for (var i = lowNum; i < highNum; i++) {
    if (i/mult == 0 && i > 0) {
        console.log(i);
    }
}
lowHighMult(2,9,3);