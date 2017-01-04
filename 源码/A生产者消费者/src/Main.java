import java.util.Scanner;
/**
 * Created by xubowen on 2016/12/25.
 */
public class Main {

    public static int bufferCount;//缓冲区个数
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入生产者个数：");
        int producerCount = scanner.nextInt();
        System.out.println("请输入消费者个数：");
        int consumerCount = scanner.nextInt();
        System.out.println("请输入缓冲区个数：");
        bufferCount = scanner.nextInt();
        System.out.println("请输入每个生产者生产产品个数：");
        int productCount = scanner.nextInt();

        Container contain = new Container();
        for (int i = 1; i <= producerCount; i++) {
            Thread productThread = new Thread(new Producer(contain,i,productCount));
            productThread.start();
        }
        for (int i = 1; i <= consumerCount; i++) {
            Thread consumerThread = new Thread(new Consumer(contain,i));
            consumerThread.start();
        }
    }
}
