package daily_algo;

import java.util.Scanner;

public class PROG_��Ʈ���� {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);				// String �Է� ó��
		String input = scan.next();
		
		int result = solution(input);						// programmers�� solution �޼ҵ� ����
		System.out.println(result);							// �� ���
	}

	private static int solution(String dartResult) {
		int answer = 0;
		
		char[] str_arr = dartResult.toCharArray();				// String => char �迭�� ��ȯ
		int str_index = 0;									// char �迭 �ε���
		int max_length = str_arr.length;					// char �迭 ����
		
		int [] score_arr = new int[4];						// ���� ���� �迭 (�ε��� 1,2,3 ���, 0�� ���)
		int score_index = 0;								// ���� ���� �迭 ���� �ε���
			
	
		// Algorithm
		// 1. ���ڸ� ������ score_arr�� �ִ´�.
		// 2. ���ڰ� 1�� ��� �ڿ� 0�� �ִ��� �˻� �� ������ score_arr[score_index]���� 10���� �ٲٰ� str_index+1�� �ؼ� �ǳʰ���.
		
		
		for (int i = str_index; i < max_length; i++) {				// ���̸�ŭ �˻��Ѵ�.
			if(str_arr[i] == '0') {									// 0�� ���
				score_index++;										// score_index 1����
				String num = str_arr[i] + "";						// char => String
				score_arr[score_index] = Integer.parseInt(num);		//String => int 
				continue;
			}
			
			if(str_arr[i] >= '1' && str_arr[i] <= '9') {			// ������ ���
				score_index++;										// score_index 1����
				if(str_arr[i] == '1') {								// 1���� 10���� �з��ϱ� ���ؼ� �˻�
					if(str_arr[i+1] == '0') {						// 10�� ���
						score_arr[score_index] = 10;				// 10�ֱ�
										
						i++;										// 0 �ǳ� �ٱ� ���� 1����
						continue;
					}
				}
				String num = str_arr[i] + "";					
				score_arr[score_index] = Integer.parseInt(num);	 
				
			}else if(str_arr[i] == 'S') {								// ���� score_arr[score_index]��  1����
				
			}else if(str_arr[i] == 'D') {								// ���� score_arr[score_index]��  2����
				score_arr[score_index] = score_arr[score_index] * score_arr[score_index];
			}else if(str_arr[i] == 'T') {								// ���� score_arr[score_index]��  3����
				score_arr[score_index] = score_arr[score_index] * score_arr[score_index] * score_arr[score_index];
			}else if(str_arr[i] == '*') {								// ��Ÿ�� : �ش� ������ �ٷ� ���� ���� ������ �� 2��, ù ���� ��ȸ�� ��Ÿ���� ��� ù ������ 2��
				if(score_index == 0) {									//ù ��° ��ȸ�� ��Ÿ���� ���
					score_arr[score_index] = score_arr[score_index] * 2;
					continue;
				}
				score_arr[score_index-1] = score_arr[score_index-1] * 2; 
				score_arr[score_index] = score_arr[score_index] * 2; 
				
			}else if(str_arr[i] == '#') {								// ������ : �ش� ������ ���̳ʽ��� �ٲ۴�.
				score_arr[score_index] = score_arr[score_index] *-1;
			}
		}
		
		answer = score_arr[1] + score_arr[2] + score_arr[3];			// 3���� ��ȸ���� ���� ���� �հ�
		
        return answer;
		
	}

}
