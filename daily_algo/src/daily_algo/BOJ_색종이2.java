package daily_algo;

import java.util.Scanner;

public class BOJ_색종이2 {

	static int map [][] = new int [102][102];			// 테두리 검사를위해 큰 도화지 
	static boolean v [][] = new boolean [102][102];		// 이미 지난곳은 체크
	static int count = 0;								// 검은색 영역의 둘레
	public static void main(String[] args) {	
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();						// 색종이 수
		
		for(int i = 0; i < N ; i++) {
			int x = scan.nextInt();
			int y = scan.nextInt();
			
			for (int r = x; r < x + 10; r++) {		//색종이 위치 1로 변경
				for (int c = y; c < y + 10; c++) {
					map[r][c] = 1;
				}
			}
		}
		 
		
		// Algorithm
		// 0인곳에서 검사하여 1만나면 count++
		
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map.length; j++) {
				if(map[i][j] == 0 && v[i][j] == false) {	// 0이면서 처음 방문한 곳
					v[i][j] = true;							// 방문 체크
					dfs(i,j);
				}
			}
		}
		System.out.println(count);
	}

	private static void dfs(int r, int c) {
		int [] dr = {-1, +1, 0, 0};		// 4방향 탐색
		int [] dc = {0, 0, -1, 1};			
		v[r][c] = true;					// 방문한 곳 체크
		
		for (int d = 0; d < 4; d++) {	// 4방향 탐색
			
			if(r + dr[d] >= 0 && c + dc[d] >= 0 && r + dr[d] < 102 && c +dc[d] < 102) {	// 맵 밖으로 안나갈때 
				
				if(v[r + dr[d]][c + dc[d]] == true) {	// 방문했던 곳은 패스
					continue;
				}
				
				if(map[r + dr[d]][c + dc[d]] == 1) {	// 1 이면 둘레 +1 하고 방문표시
					count ++;
				}else {									// 0일경우 둘레를 찾아 출발
					dfs(r + dr[d], c + dc[d]);
				}
			}
		}
	}
}
