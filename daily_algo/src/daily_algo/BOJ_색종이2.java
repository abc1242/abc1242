package daily_algo;

import java.util.Scanner;

public class BOJ_������2 {

	static int map [][] = new int [102][102];			// �׵θ� �˻縦���� ū ��ȭ�� 
	static boolean v [][] = new boolean [102][102];		// �̹� �������� üũ
	static int count = 0;								// ������ ������ �ѷ�
	public static void main(String[] args) {	
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();						// ������ ��
		
		for(int i = 0; i < N ; i++) {
			int x = scan.nextInt();
			int y = scan.nextInt();
			
			for (int r = x; r < x + 10; r++) {		//������ ��ġ 1�� ����
				for (int c = y; c < y + 10; c++) {
					map[r][c] = 1;
				}
			}
		}
		 
		
		// Algorithm
		// 0�ΰ����� �˻��Ͽ� 1������ count++
		
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map.length; j++) {
				if(map[i][j] == 0 && v[i][j] == false) {	// 0�̸鼭 ó�� �湮�� ��
					v[i][j] = true;							// �湮 üũ
					dfs(i,j);
				}
			}
		}
		System.out.println(count);
	}

	private static void dfs(int r, int c) {
		int [] dr = {-1, +1, 0, 0};		// 4���� Ž��
		int [] dc = {0, 0, -1, 1};			
		v[r][c] = true;					// �湮�� �� üũ
		
		for (int d = 0; d < 4; d++) {	// 4���� Ž��
			
			if(r + dr[d] >= 0 && c + dc[d] >= 0 && r + dr[d] < 102 && c +dc[d] < 102) {	// �� ������ �ȳ����� 
				
				if(v[r + dr[d]][c + dc[d]] == true) {	// �湮�ߴ� ���� �н�
					continue;
				}
				
				if(map[r + dr[d]][c + dc[d]] == 1) {	// 1 �̸� �ѷ� +1 �ϰ� �湮ǥ��
					count ++;
				}else {									// 0�ϰ�� �ѷ��� ã�� ���
					dfs(r + dr[d], c + dc[d]);
				}
			}
		}
	}
}
