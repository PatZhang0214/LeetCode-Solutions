import java.util.HashMap;

class TwoSum {

    public int[] twoSum(int[] nums, int target) {

        boolean found = false;
        int index = 0;
        int returnValue[] = new int[2];
        HashMap<Integer, Integer> record = new HashMap<Integer, Integer>();

        while(!found) {
            int remaining = target - nums[index];

            if(record.get(remaining) != null) {

                returnValue[0] = record.get(remaining);
                returnValue[1] = index;

                return returnValue;
 
            } else {
                record.put(nums[index], index);
            }
            index++;   
        }

        return returnValue;
    }
}