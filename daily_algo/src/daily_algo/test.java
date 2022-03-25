package daily_algo;

import java.util.Scanner;

public class test {

	public static void main(String[] args) {

		Scanner sc =  new Scanner(System.in);
		
		int inf = 99999; //Integer.MAX_VALUE;
		
		int t = sc.nextInt();	//테케 수
		
		for(int tc = 0; tc< t; tc++) {
			int n  = sc.nextInt();	//편의점 수
			
			int location [][] = new int [n+2][2];	//xy좌표값들 저장
			int fw[][] = new int [n+2][n+2];	//플로이드 와샬
			
			
			for(int i =0; i<n+2;i++) {
				location[i][0] = sc.nextInt();
				location[i][1] = sc.nextInt();
			}
			
			for(int i = 0; i<n+2; i++) {
				for(int j = 0; j< n+2; j++) {
					fw[i][j] = (Math.abs(location[i][0] - location[j][0]))+(Math.abs(location[i][1] - location[j][1]));	//맨해튼 거리 저장
					if(fw[i][j]>1000) fw[i][j] = inf;
				}
			}
			
			for(int i = 0; i<n+2; i++) {
				for(int j = 0; j< n+2; j++) {
					System.out.print(fw[i][j] + " ");
				}System.out.println();
			}
			//플로이드 와샬
			
			
			for(int k =0;k<n+2;k++) {	//경
				for(int i =0; i<n+2;i++) {	//출
					for(int j = 0; j<n+2;j++) {	//도
						
						if(fw[i][j] > fw[i][k] + fw[k][j]) {
							fw[i][j] = fw[i][k] + fw[k][j];
						}
	
					}
				}
			}
		

			
			
			
			if(fw[0][n+1] <= 1000*(n+1)) {
				System.out.println("happy");
			}else {
				System.out.println("sad");
			}
			
			
			
		}

	}
}
