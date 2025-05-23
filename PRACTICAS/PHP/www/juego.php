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

if (!isset($_GET['id'])) {
    die("ID de juego no proporcionado.");
}

$id = (int)$_GET['id'];
$stmt = $pdo->prepare("SELECT * FROM videojuego WHERE id = ?");
$stmt->execute([$id]);
$juego = $stmt->fetch();

if (!$juego) {
    die("Juego no encontrado.");
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title><?= $juego['titulo'] ?></title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <div class="row g-4 align-items-center">
            <div class="col-md-6">
                <img src="<?= $juego['portada'] ?>" alt="Portada del juego" class="img-fluid rounded shadow">
            </div>
            <div class="col-md-6">
                <h1><?= $juego['titulo'] ?></h1>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item"><strong>Género:</strong> <?= $juego['genero'] ?? 'No especificado' ?></li>
                    <li class="list-group-item"><strong>Plataforma:</strong> <?= $juego['plataforma'] ?? 'No especificada' ?></li>
                    <li class="list-group-item"><strong>Fecha de salida:</strong> <?= $juego['fecha_salida'] ?? 'Desconocida' ?></li>
                </ul>
                <a href="index.php" class="btn btn-secondary mt-4">Volver</a>
            </div>
        </div>
    </div>
</body>
</html>