// 要求一：函式與流程控制

function calculate(min, max){
    // 請用你的程式補完這個函式的區塊
    var sum = 0;
    for(var i = min;i < max + 1; i++){
        sum = sum + i;
    }
    console.log(sum)
    }
    calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
    calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

    console.log('-------------------------------------');

// 要求二：JavaScript 物件與陣列

function avg(data){
    // 請用你的程式補完這個函式的區塊
    // console.log(data)
    var arr = Object.values(data)
    var relArray = arr[1];
    var sum = 0;
    for(var i=0; i<relArray.length; i++){
        sum += relArray[i]['salary']
    }
    var average = sum / i;
    console.log(average);
    }
    avg({
    "count":3,
    "employees":[
    {
    "name":"John",
    "salary":30000
    },
    {
    "name":"Bob",
    "salary":60000
    },
    {
    "name":"Jenny",
    "salary":50000
    }
    ]
    }); // 呼叫 avg 函式

    console.log('-------------------------------------');

// 要求三：演算法

function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊
    function quickSort(nums) {
        if (nums.length ===1) {
            return nums;
        }
        var pivot = nums[nums.length - 1];
        var left = [];
        var right = [];
        for (let i = 0; i < nums.length - 1; i++){
            if (nums[i] < pivot) {
                left.push(nums[i]);
            } else {
                right.push(nums[i])
            }
        }

        if (left.length > 0 && right.length > 0){
            return [...quickSort(left), pivot, ...quickSort(right)];
        } else if (left.length > 0) {
            return [...quickSort(left), pivot];
        } else {
            return [pivot, ...quickSort(right)];
        }
        }
    var sortednums = quickSort(nums);
    var left_two_max = sortednums[0] * sortednums[1];
    var len = sortednums.length;
    var right_two_max = sortednums[len - 1] * sortednums[len - 2];
    console.log(Math.max(left_two_max, right_two_max));
}
    maxProduct([5, 20, 2, 6]) // 得到 120
    maxProduct([10, -20, 0, 3]) // 得到 30
    maxProduct([-1, 2]) // 得到 -2
    maxProduct([-1, 0, 2]) // 得到 0
    maxProduct([-1, -2, 0]) // 得到 2

    console.log('-------------------------------------');

// 要求四 ( 請閱讀英文 )：演算法

function twoSum(nums, target){
    // your code here
    for(var i = 0; i < nums.length; i++) {
        for(var j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j]
            }
        }
    }
    }
    let result=twoSum([2, 11, 7, 15], 9);
    console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
    