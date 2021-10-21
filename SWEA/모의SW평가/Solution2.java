package day1019;

/*
 * 문제
 * N개 지하철역의 이용객 숫자가 주어질 때, 타당도가 가장 높은 값이 되도록, 
 * 2개의 직통 노선을 건설하고, 이 때 타당도 값을 구하라!
 * 
 * 풀이
 * 0~(N-1)까지의 번호 중에서 A<B<C<D이며, A와 B, C와 D는 인접하지 않도록 한다. (A!=(B-1+N)%N)
 * 직통 노선 건설할 수 있는 모든 경우의 타당도를 비교하여 최댓값을 구한다.

5
10
80 90 65 55 90 60 40 35 30 25
8
30 25 70 55 95 75 90 20
10
60 85 45 25 15 70 55 70 85 35
15
80 30 35 95 45 85 30 25 100 85 10 60 80 30 5
20
45 30 5 85 55 85 10 5 75 60 15 65 45 50 75 80 15 10 50 90

#1 38425
#2 44225
#3 37925
#4 64850
#5 57850

 */

import java.util.*;
import java.io.*;

public class Solution2 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			int answer = 0;
			
			System.out.printf("#%d %d\n", t, answer);
		}
	}

}
