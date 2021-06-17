package com.liuyang.rss_redis;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;


@SpringBootApplication
@EnableDiscoveryClient
public class RssRedisApplication {

    public static void main(String[] args) {
        SpringApplication.run(RssRedisApplication.class, args);
    }

}
