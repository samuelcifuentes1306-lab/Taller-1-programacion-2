from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create("15.235.56.59", 8180)
user_id = mc.getPlayerEntityId("Samuel")
x, y, z = mc.entity.getTilePos(user_id)


CL_033 = {
    0: (block.AIR.id, 0),     # Fondo -> Transparente (Aire)
    1: (block.WOOL.id, 10),   # Morado (cuerpo)
    2: (block.WOOL.id, 6),    # Rosado (zonas claras)
    3: (block.WOOL.id, 13),   # Verde (manchas)
    4: (block.WOOL.id, 15),   # Negro (sombra muy oscura)
    5: (block.WOOL.id, 7),    # Gris (sombras)
    6: (block.WOOL.id, 10),   # Morado (tono oscuro)
    7: (block.WOOL.id, 0),    # Blanco (ojos / brillos)
    8: (block.WOOL.id, 15),   # Negro (contorno)
    9: (block.WOOL.id, 12)    # Café (pupila)
}

PK_033 = [
    [0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,8,1,8,0,0,0,0,0,0,0,0,8,8,0,0,0,0],
    [0,0,8,1,8,0,0,0,0,0,0,0,8,2,8,0,8,8,0],
    [0,0,8,1,1,8,0,0,0,0,0,0,8,2,8,8,2,8,0],
    [0,8,1,1,1,8,0,0,8,0,0,8,2,2,2,2,8,0,0],
    [0,8,1,1,1,8,0,8,2,8,0,8,2,2,3,2,8,0,0],
    [0,0,8,1,1,8,0,8,2,2,8,2,2,3,3,2,8,0,0],
    [0,0,8,1,1,1,8,2,2,4,2,2,3,3,3,8,0,0,0],
    [0,0,0,8,1,5,8,1,2,4,2,3,3,3,3,8,0,0,0],
    [0,8,8,5,5,2,2,1,2,4,2,3,3,5,2,8,8,0,0],
    [8,2,2,2,1,2,2,2,6,2,5,2,3,2,4,1,6,8,0],
    [0,8,6,1,2,2,2,2,2,2,1,2,4,4,1,1,1,8,0],
    [0,0,8,2,1,2,2,4,6,1,1,1,1,1,6,1,6,1,8],
    [0,8,2,2,6,2,4,7,6,1,5,1,1,1,1,1,5,1,8],
    [0,8,2,2,2,6,9,7,1,1,5,1,6,5,1,5,1,6,8],
    [8,2,2,2,2,1,1,1,5,5,1,6,1,1,5,8,8,7,8],
    [8,5,2,2,1,1,5,5,1,1,5,2,2,1,5,0,8,8,0],
    [0,8,8,5,5,5,7,8,8,8,5,5,5,1,8,0,0,0,0],
    [0,0,8,7,6,8,8,0,0,0,8,1,1,8,0,0,0,0,0],
    [0,0,8,8,8,0,0,0,0,8,2,2,2,8,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,8,7,7,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0]
]


mc.setBlock(x, y, z, 35, 15)


for fila in range(len(PK_033)):
    for columna in range(len(PK_033[fila])):

        color = PK_033[fila][columna]

        block_id, data = CL_033[color]

        mc.setBlock(
            x + columna,
            y + 1 + (len(PK_033) - 1 - fila),
            z,
            block_id,
            data
        )

mc.postToChat("Pixel Art PK_033 creado!")