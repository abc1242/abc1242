package daily_algo;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BOJ_회의실배정 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);		
		int N = scan.nextInt();					// 회의 수 입력 받기
		int arr[][] = new int [N][2];

		for (int i = 0; i < N; i++) {
		
			arr[i][0] = scan.nextInt();			// 회의 시작 시간
			arr[i][1] = scan.nextInt();			// 회의 종료 시간
		}
		
		int cnt = 0;							// 가능한 회의 수 체크
		int end = 0; 							// 현재 진행중인 회의 종료시간 저장
		
		// Algorithm
		// 1. 종료시간 기준으로 정렬하기
		// 2. 현재 회의 종료시간과 다음 회의 시작시간 비교후  맞으면 회의 종료 시간을 다음 회의 종료시간으로 변경
		
		Arrays.sort(arr, new Comparator<int [] >() {	// 종료시간으로 정렬하기

			@Override
			public int compare(int[] o1, int[] o2) {

				if(o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}
				
				return o1[1] -o2[1];			// 종료시간 오름차순 정렬
			}
		});
		
		for (int i = 0; i < N; i++) {			// 전체 회의 검사
			
			if(end <= arr[i][0]) {				// 종료시간보다 시작시간이 나중인 경우
				cnt ++;							// 진행가능 회의 카운트
				end = arr[i][1];				// 회의 종료시간 업데이트
			}
		}
		System.out.println(cnt);
	}

}
