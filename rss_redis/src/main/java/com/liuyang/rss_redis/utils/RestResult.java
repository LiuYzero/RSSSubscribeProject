package com.liuyang.rss_redis.utils;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * Restfule接口结果的封装类
 * @description:
 * @author: home
 * @time: 2021/6/12 11:02
 */

@ApiModel
public class RestResult<T> {

    // 状态码
    @ApiModelProperty("返回状态码")
    private String code;

    // 状态信息
    @ApiModelProperty("返回状态信息")
    private String message;

    // 返回数据
    @ApiModelProperty("返回结果")
    private T Data;

    public RestResult(String code, String message, T data) {
        this.code = code;
        this.message = message;
        Data = data;
    }

    public RestResult(String code, String message) {
        this.code = code;
        this.message = message;
    }

    public RestResult() {
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public T getData() {
        return Data;
    }

    public void setData(T data) {
        Data = data;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (!(o instanceof RestResult)) return false;

        RestResult<?> that = (RestResult<?>) o;

        return new org.apache.commons.lang3.builder.EqualsBuilder()
                .append(getCode(), that.getCode())
                .append(getMessage(), that.getMessage())
                .append(getData(), that.getData())
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new org.apache.commons.lang3.builder.HashCodeBuilder(17, 37)
                .append(getCode())
                .append(getMessage())
                .append(getData())
                .toHashCode();
    }

    @Override
    public String toString() {
        return "RestResult{" +
                "code='" + code + '\'' +
                ", message='" + message + '\'' +
                ", Data=" + Data +
                '}';
    }
}
