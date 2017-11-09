import threading
from Obstacle import Obstacle
import pygame
SPEED = 3.5


class Timer:
    def __init__(self, count, finish, stage, height):
        self.count = count
        self.finish = finish
        self.obstacle_value = False
        self.stage = stage
        self.height = height
        self.obstacles = []
        self.time = -25
        self.rhythm_function = None

    def timer(self):
        timer = threading.Timer(1, self.timer)
        self.count -= 1
        timer.start()
        if self.count == 0 or self.finish:
            timer.cancel()

    def rhythm(self):
        a = 522
        self.rhythm_function = threading.Timer(0.09, self.rhythm)
        print(self.time)
        self.time += 1
        self.rhythm_function.start()
        if self.time == 2:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 6:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 8:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 14:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
            pygame.mixer.music.unpause()
        elif self.time == 18:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 20:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 26:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 30:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 32:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 37:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 39:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 49:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 51:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 53:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 55:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 60:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 62:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 76:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 80:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 82:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 87:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 89:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 99:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 101:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 103:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 105:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 110:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 112:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 126:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 127:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 129:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 130:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 138:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 139:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 141:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 142:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 151:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 155:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 157:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 162:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 164:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 174:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 176:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 178:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 180:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 185:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 187:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 201:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 205:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 207:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 212:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 214:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 224:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 226:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 228:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 230:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 235:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 237:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 250:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 251:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 253:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 254:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 262:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 263:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 265:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 266:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 274:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 276:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 278:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 281:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 283:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 287:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 289:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 293:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 300:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 302:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 304:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 308:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 310:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 313:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 315:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 325:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 328:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 331:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 334:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 338:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 340:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 342:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 350:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 352:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 354:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 356:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 360:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 362:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 375:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 378:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 381:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 384:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 388:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 390:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 392:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 400:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 402:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 404:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 406:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 410:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 412:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 425:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 428:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 431:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 434:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 438:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 440:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 442:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 450:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 452:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 454:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 456:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 460:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 462:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 474:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 477:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 480:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 483:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 487:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 489:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 491:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 499:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 501:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 503:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 505:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 509:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 511:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 2 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 6 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 8 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 14 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 18 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 20 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 26 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 30 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 32 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 37 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 39 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 49 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 51 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 53 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 55 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 60 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 62 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 76 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 80 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 82 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 87 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 89 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 99 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 101 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 103 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 105 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 110 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 112 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 126 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 127 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 129 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 130 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 138 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 139 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 141 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 142 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 151 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 155 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 157 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 162 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 164 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 174 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 176 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 178 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 180 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 185 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 187 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 201 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 205 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 207 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 212 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 214 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 224 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 226 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 228 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 230 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 235 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 237 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 250 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 251 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 253 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 254 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 262 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 263 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 265 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 266 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 274 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 276 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 278 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 281 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 283 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 287 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 289 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 293 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 300 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 302 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 304 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 308 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 310 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 313 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 315 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 325 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 328 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 331 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 334 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 338 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 340 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 342 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 350 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 352 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 354 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 356 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 360 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 362 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 375 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 378 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 381 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 384 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 388 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 390 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 392 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 400 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 402 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 404 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 406 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 410 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 412 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 425 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 428 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 431 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 434 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 438 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 440 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 442 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 450 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 452 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 454 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 456 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 460 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 462 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 474 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 477 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 480 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 483 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 487 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 489 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 491 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 499 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 501 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 503 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 505 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 509 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 511 + a:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
        elif self.time == 524:
            obstacle = Obstacle(self.stage, self.height, SPEED)
            self.obstacles.append(obstacle)
            self.rhythm_function.cancel()
        elif self.time > 1100:
            self.rhythm_function.cancel()

    def Return(self):
        return self.count

    def ReturnObj(self):
        return self.obstacles

    def Stop(self):
        self.rhythm_function.cancel()

    def init(self):
        self.obstacles = []
