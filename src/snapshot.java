import com.googlecode.javacv.OpenCVFrameGrabber;
import com.googlecode.javacv.cpp.opencv_core;
import static com.googlecode.javacv.cpp.opencv_highgui.cvSaveImage;

public class snapshot{

public static void main(String[] args) throws Exception {

OpenCVFrameGrabber frameGrabber = new OpenCVFrameGrabber("rtsp://admin:fandi123@192.168.1.64/Stream/Channels/101/?dummy=param.mjpg"); 
        try {
            frameGrabber.start();
            opencv_core.IplImage img=frameGrabber.grab();
            if(img!=null)
            {
                cvSaveImage("Gambar.png", img);
            }
        } catch (Exception e){
            e.printStackTrace();
        }

    }

}
