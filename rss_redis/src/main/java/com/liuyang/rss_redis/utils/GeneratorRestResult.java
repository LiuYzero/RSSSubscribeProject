package com.liuyang.rss_redis.utils;

/**
 * 静态生成RestResult类
 * @description:
 * @author: home
 * @time: 2021/6/12 11:17
 */
public class GeneratorRestResult {

    public static RestResult getRestResult(String code, String message, Object data){
        return new RestResult<Object>(code, message, data);
    }
}
