import pygame


class Plane(pygame.sprite.Sprite):
    # 飞机图片
    images_src = []
    # 摧毁图片
    destroy_images_src = []
    # 摧毁音效
    destroy_sound_src = None
    # 生命
    life = 1

    def __init__(self, screen, speed=10):
        super().__init__()
        # 游戏界面
        self.screen = screen
        # 移动速度
        self.speed = speed
        # 状态
        self.active = True
        # 飞机图片对象
        self.images = list(map(lambda img: pygame.image.load(img), self.images_src))
        # 飞机摧毁图片对象
        self.destroy_images = list(map(lambda img: pygame.image.load(img), self.destroy_images_src))
        # 初始化子弹
        self.bullets = pygame.sprite.Group()
        # 初始化飞机位置
        self.rect = self.images[0].get_rect()

    def get_screen_size(self):
        return self.screen.get_size()

    def hurt(self, power=1):
        """ 被伤害 """
        self.life -= power
        if self.life <= 0:
            self.destroy()

    def destroy(self):
        """ 坠机 """
        self.active = False
        sound = pygame.mixer.Sound(self.destroy_sound_src)
        sound.play()
        # 这里是多张爆炸图片在同一帧渲染
        for image in self.destroy_images:
            self.screen.blit(image, self.rect)

    def update(self, war):
        """游戏循环"""
        self.bind_event(war.down_key)  # 绑定事件
        self.render(war)  # 渲染视图
        self.bullets.update(war)  # 更新子弹

    def bind_event(self, down_key):
        """ 绑定事件 """
        pass

    def render(self, war):
        self.screen.blit(self.images[0], self.rect)

    def move_up(self):
        """向上移动"""
        self.rect = self.rect.move(0, -self.speed)
        self.rect.top = max(0, self.rect.top)

    def move_down(self):
        """向下移动"""
        self.rect = self.rect.move(0, self.speed)
        self.rect.bottom = min(self.rect.bottom, self.get_screen_size()[1])

    def move_left(self):
        """ 向左移动 """
        self.rect = self.rect.move(-self.speed, 0)
        self.rect.left = max(0, self.rect.left)

    def move_right(self):
        """ 向右移动 """
        self.rect = self.rect.move(self.speed, 0)
        self.rect.right = min(self.rect.right, self.get_screen_size()[0])




