package daily_algo;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class BOJ_단어뒤집기2 {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		char []  S = br.readLine().toCharArray();
		
		Stack<Character> stack = new Stack<Character>();
		
		boolean in = false;
		
		for (int i = 0; i < S.length; i++) {
			
			if(S[i] == '<') { // <인 경우
				while(!stack.isEmpty()) { // stack이 비어있을 때까지 반복
					bw.append(stack.pop()); // stack에서 꺼내서 bw에 추가
				}
				in = true;
				bw.append('<');
			}else if(S[i] == '>') { // >인 경우
				
				in = false;
				bw.append('>');
				
			}else if(in == true) { // <>안에 있는 경우
				
				bw.append(S[i]);
				
			}else if(S[i] == ' ') { // 공백일 경우
				
				while(!stack.isEmpty()) { // stack이 비어있을 때까지 반복
					bw.append(stack.pop()); // stack에서 꺼내서 bw에 추가
				}
				bw.append(S[i]);
			}else{
				
				stack.add(S[i]);
				
			}
		}
		while(!stack.isEmpty()) { // stack이 비어있을 때까지 반복
			bw.append(stack.pop()); // stack에서 꺼내서 bw에 추가
		}
		bw.flush();
	}

}
