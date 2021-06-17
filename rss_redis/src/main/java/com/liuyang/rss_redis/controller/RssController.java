package com.liuyang.rss_redis.controller;

import com.alibaba.fastjson.JSONObject;
import com.liuyang.rss_redis.utils.GeneratorRestResult;
import com.liuyang.rss_redis.utils.RestResult;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.List;

/**
 * RSS的控制类
 * @description:
 * @author: home
 * @time: 2021/6/9 20:52
 */
@RestController
@RequestMapping("/redis")
@Api(value="Redis Manager", tags="Redis数据管理")
@CrossOrigin
public class RssController {
    Logger LOGGER = LoggerFactory.getLogger(RssController.class);

    @Autowired
    private RedisTemplate redisTemplate;

    @RequestMapping(value="/get/hello", method=RequestMethod.GET)
    @ApiOperation(value="Redis Test", notes = "测试Redis连接")

    public RestResult testController(){
        return GeneratorRestResult.getRestResult("200","success", "world");
    }

    @RequestMapping(value="/get/RSSSubscribeContents", method= RequestMethod.GET)
    @ApiOperation(value="获取RSSSubscribeContents下的所有内容", notes="所有内容转为字符串列表")
    public RestResult getRSSSubScriptLinkKeys(){
        List rssList = redisTemplate.opsForHash().values("RSSSubscribeContent");
        List<String> rssStringList = new ArrayList<String>();
        JSONObject jsonObject;
        for(Object rss : rssList){
            jsonObject = JSONObject.parseObject((String)rss);
            rssStringList.add(jsonObject.toString());
        }
        LOGGER.info(MessageFormat.format("invoke /get/RSSSubscribeContents return {0}", rssStringList.toString()));
        return GeneratorRestResult.getRestResult("200","success",rssStringList);
    }
}
