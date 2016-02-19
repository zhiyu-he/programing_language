package Valid;

import java.lang.reflect.Array;

/**
 * @author hezhiyu on 2/19/16.
 */
public class ValidHelper {

    public static boolean isEmpty(Object object) {

        if (object == null) {
            return true;
        }

        if (object.getClass().isArray()) {
            return Array.getLength(object) == 0;
        }
        return false;
    }
}
