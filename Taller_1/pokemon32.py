from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create("15.235.56.59", 8180)
user_id = mc.getPlayerEntityId("Samuel")
x, y, z = mc.entity.getTilePos(user_id)


CL_032 = {
    0: (block.AIR.id, 0),     # Fondo -> 
    1: (block.WOOL.id, 10),   # Morado 
    2: (block.WOOL.id, 6),    # Rosado 
    3: (block.WOOL.id, 7),    # Gris 
    4: (block.WOOL.id, 13),   # Verde 
    5: (block.WOOL.id, 10),   # Morado 
    6: (block.WOOL.id, 14),   # Rojo 
    7: (block.WOOL.id, 0),    # Blanco 
    8: (block.WOOL.id, 15)    # Negro 
}

PK_032 = [
    [0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,8,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,8,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,8,1,1,8,0,0,0,8,0,0,0,0,8,8,8,0],
    [0,0,8,1,1,8,0,8,8,1,8,0,8,8,2,2,2,8],
    [0,8,1,1,1,1,8,2,3,1,3,8,2,2,2,2,8,0],
    [0,8,1,1,1,1,3,2,3,3,2,2,2,3,3,1,1,8],
    [0,0,8,1,3,3,2,2,3,2,2,3,3,4,4,1,8,0],
    [0,0,0,8,2,3,2,3,2,2,3,4,4,4,1,8,0,0],
    [0,8,8,8,2,2,2,3,2,3,4,4,4,3,1,8,0,0],
    [8,2,2,2,1,2,2,2,2,3,4,4,1,1,3,1,8,0],
    [0,8,5,1,5,2,2,5,1,1,1,1,1,3,1,1,8,0],
    [0,8,2,5,2,2,3,7,1,1,3,3,3,1,1,1,8,0],
    [0,8,2,2,2,1,6,7,1,1,3,1,1,1,1,5,8,8],
    [0,0,8,2,2,1,1,1,3,3,1,1,3,1,1,5,1,8],
    [0,0,8,7,3,3,8,8,1,1,1,1,8,8,8,7,8,0],
    [0,0,0,8,7,5,8,0,8,2,2,8,0,0,8,8,0,0],
    [0,0,0,8,8,8,0,8,2,2,2,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,8,7,7,8,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,0]
]


mc.setBlock(x, y, z, 35, 15)


for fila in range(len(PK_032)):
    for columna in range(len(PK_032[fila])):

        color = PK_032[fila][columna]

        block_id, data = CL_032[color]

        mc.setBlock(
            x + columna,
            y + 1 + (len(PK_032) - 1 - fila),
            z,
            block_id,
            data
        )

mc.postToChat("Pixel Art PK_032 creado!")