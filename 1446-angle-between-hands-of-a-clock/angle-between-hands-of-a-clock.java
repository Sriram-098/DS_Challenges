class Solution {
    public double angleClock(int hour, int minutes) {
        int hr=30*hour;
        double min=(double)(11*minutes)/2;
        System.out.print(min);
        if(Math.abs(hr-min)<180 ){
           return Math.abs(hr-min);
        }
        return 360-Math.abs(hr-min);
    }
}