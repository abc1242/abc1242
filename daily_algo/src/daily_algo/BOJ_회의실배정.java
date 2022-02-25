package daily_algo;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BOJ_ȸ�ǽǹ��� {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);		
		int N = scan.nextInt();					// ȸ�� �� �Է� �ޱ�
		int arr[][] = new int [N][2];

		for (int i = 0; i < N; i++) {
		
			arr[i][0] = scan.nextInt();			// ȸ�� ���� �ð�
			arr[i][1] = scan.nextInt();			// ȸ�� ���� �ð�
		}
		
		int cnt = 0;							// ������ ȸ�� �� üũ
		int end = 0; 							// ���� �������� ȸ�� ����ð� ����
		
		// Algorithm
		// 1. ����ð� �������� �����ϱ�
		// 2. ���� ȸ�� ����ð��� ���� ȸ�� ���۽ð� ����  ������ ȸ�� ���� �ð��� ���� ȸ�� ����ð����� ����
		
		Arrays.sort(arr, new Comparator<int [] >() {	// ����ð����� �����ϱ�

			@Override
			public int compare(int[] o1, int[] o2) {

				if(o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}
				
				return o1[1] -o2[1];			// ����ð� �������� ����
			}
		});
		
		for (int i = 0; i < N; i++) {			// ��ü ȸ�� �˻�
			
			if(end <= arr[i][0]) {				// ����ð����� ���۽ð��� ������ ���
				cnt ++;							// ���డ�� ȸ�� ī��Ʈ
				end = arr[i][1];				// ȸ�� ����ð� ������Ʈ
			}
		}
		System.out.println(cnt);
	}

}
