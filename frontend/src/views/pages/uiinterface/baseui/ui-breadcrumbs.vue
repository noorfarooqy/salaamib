<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Breadcrumbs</h5>
        </div>
      </div>
      <!-- Breadcrumbs -->
      <div class="col-md-12">
        <div class="card card-buttons">
          <div class="card-body">
            <h5 class="card-title">Basic</h5>
            <p>
              Use an ordered or unordered list with linked list items to create a
              minimally styled breadcrumb. Use our utilities to add additional styles as
              desired.
            </p>
            <div class="rounded border p-4">
              <b-breadcrumb :items="itemsbasic" class="pre-breadcrumb"> </b-breadcrumb>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <div class="card card-buttons">
          <div class="card-body">
            <h5 class="card-title">Line Separator</h5>
            <p>
              Add <code>.breadcrumb-lineto</code> enable line separator style for a
              breadcrumb.
            </p>
            <div class="rounded border p-4">
              <b-breadcrumb :items="itemsbasic" class="pre-breadcrumb breadcrumb-line">
              </b-breadcrumb>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <div class="card card-buttons">
          <div class="card-body">
            <h5 class="card-title">Dot Separator</h5>
            <p>
              Add <code>.breadcrumb-dot</code> enable line separator style for a
              breadcrumb.
            </p>
            <div class="rounded border p-4">
              <b-breadcrumb :items="itemsbasic" class="pre-breadcrumb breadcrumb-dot">
              </b-breadcrumb>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <div class="card card-buttons">
          <div class="card-body">
            <h5 class="card-title">Without Separator</h5>
            <p>Add <code>.breadcrumb-separatorless</code> to remove the separator.</p>
            <div class="rounded border p-4">
              <b-breadcrumb :items="itemsbasic" class="pre-breadcrumb breadcrumb-separatorless">
              </b-breadcrumb>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <div class="card card-buttons">
          <div class="card-body">
            <h5 class="card-title">Colored Breadcrumb</h5>
            <p>use class <code> .breadcrumb-colored .bg-primary</code></p>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-primary"></b-breadcrumb>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-secondary"></b-breadcrumb>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-success"></b-breadcrumb>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-info"></b-breadcrumb>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-warning"></b-breadcrumb>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-danger"></b-breadcrumb>
            <b-breadcrumb :items="itemslibrary" class="breadcrumb-colored bg-dark"></b-breadcrumb>
          </div>
        </div>
      </div>
      <!-- /Breadcrumbs -->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Breadcrumbs",

      itemsbasic: [
        {
          text: "Home",
          href: "javascript:;",
        },
        {
          text: "Library",
          href: "javascript:;",
        },
        {
          text: "Active",
          active: true,
        },
      ],
      itemslibrary: [
        {
          text: "Library",
          href: "javascript:;",
        },
        {
          text: "Active",
          active: true,
        },
      ],
    };
  },
};
</script>
