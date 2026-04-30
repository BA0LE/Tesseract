import pygame
from Caculator import *
from numpy import array, sum
import itertools

pygame.init()

#setup
W, H = 500, 500
name = "Tesseract Simulator"
FPS = 60
FOV = 500
SPEED = 0.02 #s
W_dist = 2.0
NEAR = 0.1

#setup Object:
#auto generate 1 tesseract with 16 peaks
Tesseract = array(list(itertools.product([-1, 1], [-1, 1], [-1, 1], [-1, 1])), dtype=float)

Tesseract = Tesseract[:, ::-1]
#=> 32 edges
Edges = [
    (i, j) for i in range(16) for j in range(i + 1, 16) #dung ra la 16 vì có tất cả 16 đỉnh, ko cần lùi
    if sum(Tesseract[i] != Tesseract[j]) == 1 #not the same ?
]


#setup GUI

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption(name)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 14)

#mình sẽ thử sử dụng hàm main() để chạy chương trình thay vì code trần, điều đó tốt hơn nếu muốn phát triển project

def main():
    global W_dist
    camera = array([0.0, 0.0, -5.0]) #fixed positions

    #Rotations:
    angle = {
        "xy": 0.0,
        "xz": 0.0,
        "yz": 0.0,
        "xw": 0.0,
        "yw": 0.0,
        "zw": 0.0,
    }

    #
    running = True
    while running:
        clock.tick(FPS)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False #meo de develop project tot hon (cho test)
                    #nhu vay thi khi phat hien glitch, co the nhanh chong exit va fix
                
                if event.key == pygame.K_LEFTBRACKET: #worked
                    W_dist = max(1.1, W_dist - 0.1)
                if event.key == pygame.K_RIGHTBRACKET:
                    W_dist = min(5.0, W_dist + 0.1)     

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: angle["xz"] += SPEED
        if keys[pygame.K_a]: angle["xy"] -= SPEED
        if keys[pygame.K_s]: angle["xz"] -= SPEED
        if keys[pygame.K_d]: angle["xy"] += SPEED
        if keys[pygame.K_q]: angle["yz"] -= SPEED
        if keys[pygame.K_e]: angle["yz"] += SPEED
        if keys[pygame.K_r]: angle["xw"] -= SPEED
        if keys[pygame.K_t]: angle["xw"] += SPEED
        if keys[pygame.K_f]: angle["yw"] -= SPEED
        if keys[pygame.K_g]: angle["yw"] += SPEED
        if keys[pygame.K_v]: angle["zw"] -= SPEED
        if keys[pygame.K_b]: angle["zw"] += SPEED

        R4 = (rot_xy(angle["xy"])
            @ rot_xz(angle["xz"])
            @ rot_yz(angle["yz"])
            @ rot_xw(angle["xw"])
            @ rot_yw(angle["yw"])
            @ rot_zw(angle["zw"])
        )

        # Convert: 4D -> 3D -> 2D
        projected_2d = []
        depths = []

        for v4 in Tesseract:
            p4 = R4 @ v4

            p3 = projection_4d_to_3d(p4, W_dist)

            p3 = p3 - camera

            projected_2d.append(p3)
            depths.append(p3[2])
        screen.fill((15, 15, 15))

        for i, j in Edges:
            p1 = projected_2d[i]
            p2 = projected_2d[j]

            #draw if BOTH 2 peaks in front of Camera:
            if p1[2]  <= NEAR and p2[2] <= NEAR:
                continue

            x1, y1 = projection_3D_to_2D(p1, FOV, W, H)
            x2, y2 = projection_3D_to_2D(p2, FOV, W, H)

            #a little effection :)))
            depths = (p1[2] + p2[2]) / 2
            bright = max(60, min(255, int(220 - depths * 18))) #do sang theo khoang cach

            v_i, v_j = Tesseract[i], Tesseract[j]
            if v_i[3] != v_j[3]: #not the same "W" position => edge in the 4 dimentions
                color = (bright, int(bright * 0.6), 0)
            else:
                color = (0, int(bright * 0.5), bright)

            pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

        #ok, now i ll make some guids
        HUD = [
            "------------------------------------------------------------------------",
            f"Pos ({camera[0]:+.2f}, {camera[1]:+.2f}, {camera[2]:+.2f}) [FIXED]",
            f"W_Dist {W_dist:.1f} FPS {clock.get_fps():.0f}",
            f"xw = {angle["xw"]:.2f} yw = {angle["yw"]:.2f} zw = {angle["zw"]:.2f}",
            "------------------------------------------------------------------------"
        ]
        for idx, line in enumerate(HUD):
            surf = font.render(line, True, (232, 84, 84))
            screen.blit(surf, (12, 12+idx*20))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
