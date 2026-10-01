from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create("15.235.56.59", 8180)
user_id = mc.getPlayerEntityId("Samuel")
x, y, z = mc.entity.getTilePos(user_id)


CL_035 = {
    0: (block.AIR.id, 0),     # Fondo 
    1: (block.WOOL.id, 12),   # Café 
    2: (block.WOOL.id, 12),   # Café rosado 
    3: (block.WOOL.id, 6),    # Rosado 
    4: (block.WOOL.id, 7),    # Gris
    5: (block.WOOL.id, 6),    # Rosado oscuro 
    6: (block.WOOL.id, 0),    # Blanco 
    7: (block.WOOL.id, 8),    # Gris Claro 
    8: (block.WOOL.id, 15)    # Negro 
}

PK_035 = [
    [0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,8,1,8,0,8,8,8,0,0,0,0,0,0,0,0,0],
    [0,0,8,1,1,8,3,3,3,8,0,0,0,0,0,0,0,0],
    [0,0,8,3,4,3,3,3,3,3,8,8,8,8,8,8,0,0],
    [0,0,8,3,4,5,3,4,3,3,5,3,3,1,1,8,0,0],
    [0,0,8,3,3,4,4,5,3,3,3,3,3,1,4,8,8,0],
    [0,8,5,6,3,3,3,3,3,3,3,3,3,4,4,5,5,8],
    [0,8,3,8,3,3,3,6,3,5,3,3,4,4,4,5,8,0],
    [8,7,3,3,3,3,3,8,3,5,3,4,4,4,2,2,8,0],
    [8,6,3,3,4,4,3,5,3,3,3,5,3,4,2,2,2,8],
    [8,2,3,3,5,2,3,3,3,3,3,3,5,5,4,4,4,8],
    [0,8,3,3,3,3,3,3,2,3,3,3,5,5,4,2,8,0],
    [0,8,5,5,3,3,3,4,6,7,3,5,5,5,4,2,8,0],
    [0,0,8,5,3,3,3,3,4,4,5,5,5,4,2,2,8,0],
    [0,8,6,4,5,5,5,5,5,5,5,5,5,4,2,8,0,0],
    [0,0,8,8,8,4,5,5,5,5,5,5,4,2,4,8,0,0],
    [0,0,0,0,0,8,8,5,5,5,5,4,8,8,8,0,0,0],
    [0,0,0,0,0,0,0,8,6,6,8,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,0]
]


mc.setBlock(x, y, z, 35, 15)


for fila in range(len(PK_035)):
    for columna in range(len(PK_035[fila])):

        color = PK_035[fila][columna]

        block_id, data = CL_035[color]

        mc.setBlock(
            x + columna,
            y + 1 + (len(PK_035) - 1 - fila),
            z,
            block_id,
            data
        )

mc.postToChat("Pixel Art PK_035 creado!")