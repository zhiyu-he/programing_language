package ok.main;

import okhttp3.*;

/**
 * @author hezhiyu on 2/17/16.
 */
public class Go {

    public static void main(String[] args) throws Exception {
        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url("http://www.baidu.com")
                .build();

        Response response = client.newCall(request).execute();
        System.out.println(response.headers());


        MediaType JSON = MediaType.parse("application/x-protobuf; charset=utf-8");
        RequestBody body = RequestBody.create(JSON, "abc");

    }
}
