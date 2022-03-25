package daily_algo;

import java.util.Scanner;

public class BOJ_스위치켜고끄기 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);		
		
		int switchnum = scan.nextInt();
		
		int arr [] = new int[switchnum + 1]; // 배열 인덱스 1부터 사용
		
		for (int i = 1; i < arr.length; i++) { // 배열 입력 받기
			arr[i] = scan.nextInt();
		}
		
		int stdnum = scan.nextInt(); 		// 학생 수 입력 받기
		
		for (int i = 0; i < stdnum; i++) { // 학생 수만큼 반복
			
			int mw = scan.nextInt();
			
			// Algorithm
			// 남자는 배수 여자는 옆으로 검사 
			// 단순 구현 문제
			
			
			if(mw == 1) { 				// 남자인 경우
				
				int n = scan.nextInt(); // 입력 받은 수
				int n1 = n;				// 배수 증가 시 사용
				while(n <= switchnum) {
					
					if(arr[n]== 0) {
						arr[n] = 1;
					}else {
						arr[n] = 0;
					}
					n += n1;			// 배수 증가
				}
			}else { 						// 여자인 경우
				
				int n = scan.nextInt();		// 입력 받은 수
				
				int cnt = 0;
				
				while(n + cnt <= switchnum && n - cnt > 0 && arr[n + cnt] == arr[n - cnt]) { // 배열 범위내 양옆으로 검사
					
				
						if(arr[n + cnt] == 0) {
							arr[n + cnt] = 1;
							arr[n - cnt] = 1;
						}else {
							arr[n + cnt] = 0;
							arr[n - cnt] = 0;
						}
				
					cnt++;							// 다음 양옆 검사
				}
			}
		}
		
		for (int i = 1; i < arr.length; i++) {
			if(i == arr.length - 1) {			//마지막 출력후 종료
				System.out.print(arr[i]);
				break;
			}
			if(i % 20 == 0) {					//	20번째 출력후 줄바꿈
				System.out.println(arr[i]);
			}else {
				System.out.print(arr[i] + " ");	// 출력  빈칸
			}
		}
	}
}
