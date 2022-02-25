package daily_algo;

import java.util.Scanner;

public class PROG_다트게임 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);				// String 입력 처리
		String input = scan.next();
		
		int result = solution(input);						// programmers식 solution 메소드 생성
		System.out.println(result);							// 답 출력
	}

	private static int solution(String dartResult) {
		int answer = 0;
		
		char[] str_arr = dartResult.toCharArray();				// String => char 배열로 변환
		int str_index = 0;									// char 배열 인덱스
		int max_length = str_arr.length;					// char 배열 길이
		
		int [] score_arr = new int[4];						// 점수 관리 배열 (인덱스 1,2,3 사용, 0은 비움)
		int score_index = 0;								// 점수 관리 배열 현재 인덱스
			
	
		// Algorithm
		// 1. 숫자를 만나면 score_arr에 넣는다.
		// 2. 숫자가 1일 경우 뒤에 0이 있는지 검사 후 있으면 score_arr[score_index]값을 10으로 바꾸고 str_index+1을 해서 건너간다.
		
		
		for (int i = str_index; i < max_length; i++) {				// 길이만큼 검사한다.
			if(str_arr[i] == '0') {									// 0인 경우
				score_index++;										// score_index 1증가
				String num = str_arr[i] + "";						// char => String
				score_arr[score_index] = Integer.parseInt(num);		//String => int 
				continue;
			}
			
			if(str_arr[i] >= '1' && str_arr[i] <= '9') {			// 숫자일 경우
				score_index++;										// score_index 1증가
				if(str_arr[i] == '1') {								// 1인지 10인지 분류하기 위해서 검사
					if(str_arr[i+1] == '0') {						// 10인 경우
						score_arr[score_index] = 10;				// 10넣기
										
						i++;										// 0 건너 뛰기 위해 1증가
						continue;
					}
				}
				String num = str_arr[i] + "";					
				score_arr[score_index] = Integer.parseInt(num);	 
				
			}else if(str_arr[i] == 'S') {								// 현재 score_arr[score_index]값  1제곱
				
			}else if(str_arr[i] == 'D') {								// 현재 score_arr[score_index]값  2제곱
				score_arr[score_index] = score_arr[score_index] * score_arr[score_index];
			}else if(str_arr[i] == 'T') {								// 현재 score_arr[score_index]값  3제곱
				score_arr[score_index] = score_arr[score_index] * score_arr[score_index] * score_arr[score_index];
			}else if(str_arr[i] == '*') {								// 스타상 : 해당 점수와 바로 전에 얻은 점수를 각 2배, 첫 번재 기회에 스타상일 경우 첫 점수만 2배
				if(score_index == 0) {									//첫 번째 기회가 스타상일 경우
					score_arr[score_index] = score_arr[score_index] * 2;
					continue;
				}
				score_arr[score_index-1] = score_arr[score_index-1] * 2; 
				score_arr[score_index] = score_arr[score_index] * 2; 
				
			}else if(str_arr[i] == '#') {								// 아차상 : 해당 점수는 마이너스로 바꾼다.
				score_arr[score_index] = score_arr[score_index] *-1;
			}
		}
		
		answer = score_arr[1] + score_arr[2] + score_arr[3];			// 3번의 기회에서 얻은 점수 합계
		
        return answer;
		
	}

}
