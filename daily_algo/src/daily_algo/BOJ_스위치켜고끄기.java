package daily_algo;

import java.util.Scanner;

public class BOJ_����ġ�Ѱ���� {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);		
		
		int switchnum = scan.nextInt();
		
		int arr [] = new int[switchnum + 1]; // �迭 �ε��� 1���� ���
		
		for (int i = 1; i < arr.length; i++) { // �迭 �Է� �ޱ�
			arr[i] = scan.nextInt();
		}
		
		int stdnum = scan.nextInt(); 		// �л� �� �Է� �ޱ�
		
		for (int i = 0; i < stdnum; i++) { // �л� ����ŭ �ݺ�
			
			int mw = scan.nextInt();
			
			// Algorithm
			// ���ڴ� ��� ���ڴ� ������ �˻� 
			// �ܼ� ���� ����
			
			
			if(mw == 1) { 				// ������ ���
				
				int n = scan.nextInt(); // �Է� ���� ��
				int n1 = n;				// ��� ���� �� ���
				while(n <= switchnum) {
					
					if(arr[n]== 0) {
						arr[n] = 1;
					}else {
						arr[n] = 0;
					}
					n += n1;			// ��� ����
				}
			}else { 						// ������ ���
				
				int n = scan.nextInt();		// �Է� ���� ��
				
				int cnt = 0;
				
				while(n + cnt <= switchnum && n - cnt > 0 && arr[n + cnt] == arr[n - cnt]) { // �迭 ������ �翷���� �˻�
					
				
						if(arr[n + cnt] == 0) {
							arr[n + cnt] = 1;
							arr[n - cnt] = 1;
						}else {
							arr[n + cnt] = 0;
							arr[n - cnt] = 0;
						}
				
					cnt++;							// ���� �翷 �˻�
				}
			}
		}
		
		for (int i = 1; i < arr.length; i++) {
			if(i == arr.length - 1) {			//������ ����� ����
				System.out.print(arr[i]);
				break;
			}
			if(i % 20 == 0) {					//	20��° ����� �ٹٲ�
				System.out.println(arr[i]);
			}else {
				System.out.print(arr[i] + " ");	// ���  ��ĭ
			}
		}
	}
}
