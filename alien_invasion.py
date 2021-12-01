import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alients()
            self._update_screen()

    def _check_events(self):
        """响应键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_evens(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_evens(event)

    def _check_keydown_evens(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_Left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_evens(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_Left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """跟新子弹的位置并删除消失的子弹"""
        # 跟新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_alients(self):
        """跟新外星人的位置"""

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可以容纳多少个外星人
        aline = Alien(self)
        aline_width = aline.rect.width
        available_space_x = self.settings.screen_width - (2 * aline_width)
        number_aliens_x = available_space_x // (2 * aline_width)

        # 计算屏幕可以容纳多少行外星人
        aline_height = aline.rect.height
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * aline_height) - ship_height
        number_rows = available_space_y // (2 * aline_height)

        # 创建第一行的外星人
        for row_number in range(number_rows):
            for aline_number in range(number_aliens_x):
                # 创建第一行外星人
                self._creat_aline(aline_number, row_number)

    def _creat_aline(self, aline_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * aline_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 绘制飞船
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
