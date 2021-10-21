package day1019;

import java.util.*;
import java.io.*;

/*
2
5
0 1 0 0 1
1 1 0 0 0
0 1 1 0 1
0 0 2 0 0
1 0 1 1 0
10
0 1 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 1 1 0 1 0 0 1 0 0
0 0 0 0 1 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 0 0 2 0 1 0 1 0
0 0 0 0 0 0 1 0 0 0
1 0 1 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0 1 0
0 1 0 0 1 0 1 1 0 0
 */
public class Solution1 {
	
	static int N, map[][], start[], answer;
	static int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1}; // 상 우 하 좌
	static boolean[][] v; // 먹을 수 있는 알들 방문체크

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			v = new boolean[N][N];
			answer = 0;
			
			// 장기판 상태 입력받기
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					// 포? 암튼 움직일 수 있는 말 좌표 저장
					if(map[i][j]==2) start = new int[] {i, j};
				}
			}
			
			// 모든 경우의 수 따져주기
			dfs(start[0], start[1], 0);
			
			System.out.printf("#%d %d\n", t, answer);
		}
	}

	private static void dfs(int r, int c, int time) {
		// 세번 옮겼다? => 리턴해서 해당 경우는 그만 세기
		if(time==3) {
			return;
		}
		
		// 모든 방향을 탐색한다
		for (int d = 0; d < dc.length; d++) {
			int cnt = 0; // 해당 방향의 알의 수
			
			// nr, nc => 다음 이동할 위치
			int nr = r+dr[d]; int nc = c+dc[d];
			
			// 판을 벗어나지 않는 한에서 반복문 돌기
			while(isSafe(nr, nc)) {
				
				if(map[nr][nc]==1) cnt+=1; // 만약 빈칸이 아니면 알의 수 카운트해주기
				
				if(cnt==1 && map[nr][nc]==0) { // 만약 알을 하나 넘고 빈칸에 도달해서 이동하기
					// 이동 시 map에 업데이트 해주기
					map[nr][nc]=2;
					map[r][c]=0;
					
					dfs(nr, nc, time+1);
					
					// 백트래킹
					map[nr][nc]=0;
					map[r][c]=2;
				}
				
				if(cnt==2 && map[nr][nc]==1) { // 만약 알을 하나 넘고 그 다음 바로 알을 만나면 알 먹고 이동하기
					// 이동 시 map에 업데이트 해주기
					map[nr][nc]=2;
					map[r][c]=0;
					
					// 만약 이전 경우에 먹은 알이 아니면 먹은 표시해주기
					if(!v[nr][nc]) {						
						answer +=1;
						v[nr][nc]=true;
					}
					dfs(nr, nc, time+1);
					
					// 백트래킹
					map[nr][nc]=1;
					map[r][c]=0;
				}
				
				// 만약 알 두개를 넘어가는 위치면 반복문 끝내기
				if(cnt>=2) break;
				
				// 해당 방향으로 한 칸 더 가기
				nr += dr[d]; nc +=dc[d];
			}
		}
	}
	
	// 판을 넘어서는지 판단해주는 메소드
	public static boolean isSafe(int r, int c) {
		if(r<0 || r>=N || c<0 || c>=N) return false;
		return true;
	}

}
