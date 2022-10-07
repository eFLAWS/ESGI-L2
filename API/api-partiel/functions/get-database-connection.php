<?php

function getDatabaseConnection() {
    $driver = "mysql";

    $databaseName = "api-partiel";

    $hostName = "localhost";

    $dataSourceName = "$driver:dbname=$databaseName;host=$hostName";

    $username = "root";

    $password = "root";

    $options = [
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ];

    $databaseConnection = new PDO($dataSourceName, $username, $password, $options);

    return $databaseConnection;
}