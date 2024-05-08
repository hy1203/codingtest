using System;

public class Solution {
    public int solution(int num1, int num2) {
        return num1+num2;
    }
    public void Main(string[] args){
        int num1 = int.Parse(Console.ReadLine());
        int num2 = int.Parse(Console.ReadLine());
        
        int answer = solution(num1,num2);
        
        Console.WriteLine(answer);
    }
}