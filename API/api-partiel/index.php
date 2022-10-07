<?php

ini_set ('display_errors', 1);
ini_set ('display_startup_errors', 1);
error_reporting (E_ALL);

$route = $_REQUEST["route"] ?? "undefined";

$method = $_SERVER["REQUEST_METHOD"];

if ($route === "analytics") {

    if ($method === "DELETE") {
        include __DIR__ . "/controllers/analytics/delete.php";
        die();
    }
    if ($method === "GET") {
        include __DIR__ . "/controllers/analytics/get.php";
        die();
    }
    if ($method === "PATCH") {
        include __DIR__ . "/controllers/analytics/patch.php";
        die();
    }
    if ($method === "POST") {
        include __DIR__ . "/controllers/analytics/post.php";
        die();
    }
}

if ($route === "applications") {

    if ($method === "DELETE") {
        include __DIR__ . "/controllers/applications/delete.php";
        die();
    }
    if ($method === "GET") {
        include __DIR__ . "/controllers/applications/get.php";
        die();
    }
    if ($method === "PATCH") {
        include __DIR__ . "/controllers/applications/patch.php";
        die();
    }
    if ($method === "POST") {
        include __DIR__ . "/controllers/applications/post.php";
        die();
    }
} 
/*
if ($route === "login") {

    if ($method === "POST") {
        include __DIR__ . "/controllers/login/post.php";
        die();
    }
}

if ($route === "logout") {

    if ($method === "POST") {
        include __DIR__ . "/controllers/logout/post.php";
        die();
    }
}
*/
if ($route === "reports") {

    if ($method === "DELETE") {
        include __DIR__ . "/controllers/reports/delete.php";
        die();
    }
    if ($method === "GET") {
        include __DIR__ . "/controllers/reports/get.php";
        die();
    }
    if ($method === "PATCH") {
        include __DIR__ . "/controllers/reports/patch.php";
        die();
    }
    if ($method === "POST") {
        include __DIR__ . "/controllers/reports/post.php";
        die();
    }
}

if ($route === "users") {

    if ($method === "DELETE") {
        include __DIR__ . "/controllers/users/delete.php";
        die();
    }
    if ($method === "GET") {
        include __DIR__ . "/controllers/users/get.php";
        die();
    }
    if ($method === "PATCH") {
        include __DIR__ . "/controllers/users/patch.php";
        die();
    }
    if ($method === "POST") {
        include __DIR__ . "/controllers/users/post.php";
        die();
    }
}

include __DIR__ . "/functions/json-response.php";

jsonResponse(404, [], ["success" => false, "error" => "Not found"]);

