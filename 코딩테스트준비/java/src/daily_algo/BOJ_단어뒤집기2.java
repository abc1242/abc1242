package daily_algo;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class BOJ_�ܾ������2 {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		char []  S = br.readLine().toCharArray();
		
		Stack<Character> stack = new Stack<Character>();
		
		boolean in = false;
		
		for (int i = 0; i < S.length; i++) {
			
			if(S[i] == '<') { // <�� ���
				while(!stack.isEmpty()) { // stack�� ������� ������ �ݺ�
					bw.append(stack.pop()); // stack���� ������ bw�� �߰�
				}
				in = true;
				bw.append('<');
			}else if(S[i] == '>') { // >�� ���
				
				in = false;
				bw.append('>');
				
			}else if(in == true) { // <>�ȿ� �ִ� ���
				
				bw.append(S[i]);
				
			}else if(S[i] == ' ') { // ������ ���
				
				while(!stack.isEmpty()) { // stack�� ������� ������ �ݺ�
					bw.append(stack.pop()); // stack���� ������ bw�� �߰�
				}
				bw.append(S[i]);
			}else{
				
				stack.add(S[i]);
				
			}
		}
		while(!stack.isEmpty()) { // stack�� ������� ������ �ݺ�
			bw.append(stack.pop()); // stack���� ������ bw�� �߰�
		}
		bw.flush();
	}

}
