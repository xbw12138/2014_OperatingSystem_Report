/**
 * Created by xubowen on 2016/12/25.
 */
public class Producer implements Runnable {
    private Container contain = null;
    private int namei;
    private int productCount;
    public Producer(Container contain,int namei,int productCount) {
        super();
        this.contain = contain;
        this.namei=namei;
        this.productCount=productCount;
    }
    public void run() {
        while (true) {
            synchronized (contain) {
                while (contain.isFull()) {
                    try {
                        contain.wait();// 阻塞当前线程,当前线程进入等待队列。这个时候只有等待别的线程来唤醒自己了。
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
            producer();// 生产一个产品
            try {
                Thread.sleep((long) (1000));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (contain) {
                contain.notify();// 唤醒等待队列中正在等待的第一个线程，让其执行。
            }
        }
    }
    public void producer() {
        for(int i=1;i<=productCount;i++){
            Product aProduct = new Product("生产者代号 ## " + namei +" ##   生产了产品代号 ** "+i+" **");
            System.out.println(aProduct.toString());
            contain.push(aProduct);
            //System.out.println("%%%%%%%%%%%"+contain.size()+"%%%%%%%%%%");
        }
    }
}
