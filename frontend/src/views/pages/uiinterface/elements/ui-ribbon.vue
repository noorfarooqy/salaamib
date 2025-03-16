<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <element-breadcrumb :title="title" />
        <div class="row">
          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-primary">Ribbon</div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-secondary">Ribbon</div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-success">Ribbon</div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-primary ribbon-right">Ribbon</div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-secondary ribbon-right">Ribbon</div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-success ribbon-right">Ribbon</div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-vertical-left-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-primary ribbon-vertical-left">
                  <i class="fas fa-gift"></i>
                </div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-vertical-left-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-secondary ribbon-vertical-left">
                  <i class="fas fa-gift"></i>
                </div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-vertical-left-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-success ribbon-vertical-left">
                  <i class="fas fa-gift"></i>
                </div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-vertical-right-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-primary ribbon-vertical-right">
                  <i class="fas fa-gift"></i>
                </div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-vertical-right-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-secondary ribbon-vertical-right">
                  <i class="fas fa-gift"></i>
                </div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->

          <!-- Ribbon -->
          <div class="col-md-4 col-sm-6">
            <div class="ribbon-vertical-right-wrapper card">
              <div class="card-body">
                <div class="ribbon ribbon-success ribbon-vertical-right">
                  <i class="fas fa-gift"></i>
                </div>
                <p>
                  {{ content }}
                </p>
              </div>
            </div>
          </div>
          <!-- /Ribbon -->
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Ribbons",
      content:
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text. Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
      items: [
        {
          text: "Dashboard",
          href: "/index",
        },
        {
          text: "Components",
          active: true,
        },
      ],
    };
  },
};
</script>
