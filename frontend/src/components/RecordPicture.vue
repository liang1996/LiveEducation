<template>
    <Card padding="0">
        <div class="picture">
            <a @click="recordRoom">
                <div class="for-img">
                    <img :src="this.route" width="100%">
                </div>
                <div id="information">
                    <label id="information-room-name">房间名:&nbsp{{ this.roomName }}</label>
                    <br>
                    <label id="information-teacher-name">主讲教师:&nbsp{{ this.teacherName }}</label>
                </div>
            </a>
        </div>
    </Card>
</template>

<script>
/**
 * 表示录播房间的缩略图，
 * 包含老师上传的封面图片及房间信息（房间名称、老师名称），
 * 作为子组件插入首页或录播详情页。
 *
 * @module RecordPicture
 * @class RecordPicture
 */
import myMsg from './../warning.js'
export default {
    name: 'RecordPicture',
    /**
     * 表示房间名称
     *
     * @property roomName
     * @type String
     */

    /**
     * 表示创建该房间的老师名字
     *
     * @property teacherName
     * @type String
     */

    /**
     * 表示房间缩略图
     *
     * @property userImg
     * @type String
     */

    /**
     * 表示对应直播房间的ID
     *
     * @property liveId
     * @type String
     */
    props: ['roomName', 'teacherName', 'userImg', 'liveId'],
    components: {},
    data: function () {
        return {
            /**
             *表示用户是否登录
             *
             * @attribute canWork
             * @type Boolean
             * @default false
             */
            canWork: false,
            /**
             * 用来表示房间缩略图的路径
             *
             * @attribute route
             * @type String
             * @default ''
             */
            route: ''
        }
    },
    /**
     * created函数，判断用户是否登录
     *
     * @method created
     */
    created: function () {
        fetch('/getName/', {
            method: 'post',
            mode: 'cors',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json, text/plain, */*',
                'Accept': 'application/json'
            },
            body: JSON.stringify({})
        }).then((response) => response.json()).then((obj) => {
            if (obj.result) {
                this.canWork = true
            }
        })
        this.route = '/static/cover/' + this.userImg
    },
    methods: {
        /**
         * 进入录播房间，
         * 如果用户没有登录，则弹出消息框提示。
         *
         * @method recordRoom
         */
        recordRoom: function () {
            if (this.canWork) {
                window.open('./#/record_room/' + this.liveId)
            } else {
                this.$Message.error(myMsg.account['loginNeeded'])
            }
        }
    }
}

</script>

<style scoped>
.picture {
    width: 100%;
    font-size: 14px;
    text-align: left;
    overflow: hidden;
}

.for-img {
    width: 240px;
    height: 150px;
    overflow: hidden;
    border-top-right-radius: 4px;
    border-top-left-radius: 4px;
}

.for-img img {
    min-height: 150px;
}

#information {
    height: 47px;
}

#information-room-name {
    padding-left: 6px;
}

#information-teacher-name {
    padding-left: 5px;
}

.picture a {
    color: #464c5b;
}

.picture:hover {
    color: #22313F;
}
</style>
