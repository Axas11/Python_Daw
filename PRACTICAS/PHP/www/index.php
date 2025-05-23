<?php
try {
    $pdo = new PDO(
        'mysql:host=db;port=3306;dbname=juegos;charset=utf8',
        'usuario',
        'pass',
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]
    );
} catch (PDOException $e) {
    die('Error de conexión a la base de datos: ' . $e->getMessage());
}

$stmt = $pdo->query("SELECT id, titulo, portada FROM videojuego");
$videojuegos = $stmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Videojuegos</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <div class="container py-4">
        <h1 class="mb-4 text-center">Videojuegos Disponibles</h1>
        <div class="row g-4">
            <?php foreach ($videojuegos as $juego): ?>
                <div class="col-md-4">
                    <div class="card h-100 shadow">
                        <img src="<?= $juego['portada']; ?>" class="card-img-top" style="height: 300px; object-fit: cover;">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title"><?= $juego['titulo']; ?></h5>
                            <a href="juego.php?id=<?= $juego['id'] ?>" class="btn btn-primary mt-auto">Ver juego</a>
                        </div>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</body>
</html>