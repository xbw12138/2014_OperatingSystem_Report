/**
 * Created by xubowen on 2016/12/25.
 */
public class Consumer implements Runnable {
    private Container contain = null;
    private int namei;
    public Consumer(Container contain,int namei) {
        super();
        this.contain = contain;
        this.namei=namei;
    }
    public void run() {
        while (true) {
            synchronized (contain) {
                while (contain.isEmpty()) {
                    try {
                        contain.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
            consume();//消费
            try {
                Thread.sleep((long) (1000));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (contain) {
                contain.notify();
            }
        }
    }
    private void consume() {
        Product a = (Product) contain.pop();
        System.out.println("消费者代号@ "+namei+" @消费了一个产品（" + a.toString()+"）");
    }
}